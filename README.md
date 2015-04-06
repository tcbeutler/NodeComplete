#NodeComplete
  
###Auto-complete suggestions for nodejs development in Sublime Text 3.

#####Current Features
	
1. "require(..)" statement completion on open projects and folders.
  * Begin typing "require" to see a list of importable modules from your current package. Relative path calculation is done automatically.
  * Regular expression matching can be used for quickly requiring a module.
  
  ![Input match on regular expression](http://i.imgur.com/l03I7Hb.png)
  
  ![...on pressing enter, relative path completion](http://i.imgur.com/ntFoNgB.png)

#####Coming Features
BIGIFX - **Change so "curDir/..." is "./curDir/..."**  
1. Build require functionality into command pallate
2. Add options to turn on or off require completions in commmand pallate and/or completion prompts.
3. Add code completion of core nodejs modules on prompts
  * Ex: Only add "fs" prompts when "fs." is the prefix for completion.
4. Configurable exclude directories for require completion.
5. Include top level packages from node_modules
6. Update package.json so people can find this thing
7. Publish in npm
