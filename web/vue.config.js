const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    proxy: {
      '/admin': {
        target: 'http://localhost:8000', // Serverul Django
        changeOrigin: true,
      },
    },
  },
};
