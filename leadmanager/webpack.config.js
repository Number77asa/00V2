var webpack = require('webpack');

module.exports = {
    watchOptions: {
        poll: true,
        ignored: /node_modules/
    },   




    module: {
        rules: [
            {
                test:/\.js$/, /*says for any javscript file*/
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader" /*esto se va encargar de usar babel loader to traspile our code*/
                }
            }
        ]
    }
}
