import sublime_plugin
import sublime
import os

ignoredDirectories = ['node_modules', 'swagger', 'generators']

class NodeComplete(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        currentFile = sublime.active_window().active_view().file_name()
        #Only search on this drive.
        folders = [folder for folder in sublime.active_window().folders() if folder[0] == currentFile[0]]
        
        #map returns a list of list, flatten this
        files = [f for sublist in map(self.getFiles, folders) for f in sublist]

        if (prefix in 'require'):
            relativePaths = ['require("{0}")'.format(os.path.relpath(fileName, currentFile).replace('\\', '/')) for fileName in files]
            return [(rp, rp) for rp in relativePaths]
        return []

    def getFiles(self, folder):
        files = []
        for rootDirectory, subDirectories, directoryFiles in os.walk(folder):
            subDirectories[:] = [directory for directory in subDirectories if directory not in ignoredDirectories]
            files = files + [os.path.join(rootDirectory, fileName) for fileName in directoryFiles if fileName[-3:] == '.js']
        return files