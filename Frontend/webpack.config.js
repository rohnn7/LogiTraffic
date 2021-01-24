const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: ["babel-polyfill",'./src/js/index.js','./src/ckeditor_4.14.1_standard_easyimage/ckeditor/ckeditor.js'],
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: 'js/bundle.js'
    },
    devServer: {
        contentBase: './dist'        
    },
    plugins:[
        new HtmlWebpackPlugin({
            filename: 'dashboard.html',
            template: './src/dashboard.html'            
        }),
        new HtmlWebpackPlugin({
            filename: 'login.html',
            template: './src/login.html'            
        }),
        new HtmlWebpackPlugin({
            filename: 'test.html',
            template: './src/test.html'            
        }),
        new HtmlWebpackPlugin({
            filename: 'tes.html',
            template: './src/test2.html'            
        }),
    ],
    module: {
        rules: [
            {
                test:/\.js$/,
                exclude: /node_modules/,
                use:{
                    loader: 'babel-loader'
                }
            }
        ]
    }
}