import sublime_plugin
import sublime
import re

class NodeComplete(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        print(sublime.active_window().project_data())
        if (prefix in 'require'):
            return [('require("app/dependency")', "require('../../../dependency')")]
        return []