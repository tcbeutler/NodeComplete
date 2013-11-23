import sublime_plugin
import sublime
import os

ignoredDirectories = ['node_modules', 'swagger', 'generators']
requireWordSeparators = "./\\\"-:,.;<>~!@#$%^&*|+=[]{}`~?"

class NodeComplete(sublime_plugin.EventListener):
    """
    For "require" statements, add autocompletion of modules in current open folders.
    This is to make relative paths much easier to require.
    """
    def on_query_completions(self, view, prefix, locations):
        if (prefix in 'require'):

            currentFile = sublime.active_window().active_view().file_name()
            #Only search on this drive.
            folders = [folder for folder in sublime.active_window().folders() if folder[0] == currentFile[0]]
            
            #map returns a list of lists, flatten this
            files = [f for sublist in map(self.getFiles, folders) for f in sublist]

            relativePaths = ["require('{0}')".format(os.path.relpath(fileName, currentFile)) for fileName in files]
            return [self.formatQueryCompletionPath(rp) for rp in relativePaths]

        return []

    def getFiles(self, folder):
        files = []
        for rootDirectory, subDirectories, directoryFiles in os.walk(folder):
            subDirectories[:] = [directory for directory in subDirectories if directory not in ignoredDirectories]
            files = files + [os.path.join(rootDirectory, fileName) for fileName in directoryFiles if fileName[-3:] == '.js']
        return files

    def formatQueryCompletionPath(self, path):
        #Force forward slashes, remove extension and don't display '../' groups.
        newPath = path.replace('\\', '/').replace('.js', '');
        matchPath = newPath.replace('../', '')
        return (matchPath, newPath)
        