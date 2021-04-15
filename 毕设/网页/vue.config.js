module.exports = {
	/*
  "transpileDependencies": [
    "vuetify"
  ],*/
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000', // Flask的端口
        ws: true,
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''  //通过pathRewrite重写地址，将前缀/api转为/
        }
      }
    }
  },
}