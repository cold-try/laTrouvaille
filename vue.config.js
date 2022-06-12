//const { defineConfig } = require('@vue/cli-service')
//module.exports = defineConfig({
  //transpileDependencies: true
//})

const pages = {   
  index: "src/main.js",   
};  

/*
module.exports = {   
  publicPath: "https://dudtfwleya78z.cloudfront.net",
  outputDir: "build",
  assetsDir: "static", 
  indexPath: "../templates/vue_index.html",
  pages: pages,
};
*/


module.exports = {   
  publicPath: "/static/vue/", 
  outputDir: "./build/static/vue/", 
  indexPath: "../../templates/vue_index.html", 
  pages: pages,   
};