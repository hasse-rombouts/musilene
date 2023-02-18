/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js}', './node_modules/flowbite/**/*.js'],
  theme: {
    extend:
    {
      fontFamily: {
        'opensans': ['Open Sans', 'sans-serif'],
        'raleway': ['Raleway', 'sans-serif'],
        'holtwood': ['Holtwood One SC', 'serif']
      },
    },
  },

  plugins: [
    require('flowbite/plugin')
  ]
}
