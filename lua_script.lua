function main(splash)
    splash:go(splash.args.url)
    splash:wait(1)
    -- Execute your Lua script code here
    print("Lua script execution successful!")
    splash:runjs("document.title = 'Modified Title';")
    return splash:html()
end