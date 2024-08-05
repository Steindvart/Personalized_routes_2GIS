import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03'
  //, devtools: { enabled: true }
  , app: {
    head: {
      script: [
        {
          src: 'https://mapgl.2gis.com/api/js',
          async: true,
        }
      ],
    },
  }
  , build: {
    transpile: ['vuetify'],
  }
  , modules: [
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
  ]
  , vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
})
