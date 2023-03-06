/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        opensans: ["Open Sans", "sans-serif"],
        raleway: ["Raleway", "sans-serif"],
        holtwood: ["Holtwood One SC", "serif"],
      },

      animation: {
        fadeIn: "fadeIn 1s ease-in forwards",
      },
      keyframes: {
        fadeIn: {
          "0%": { opacity: 0 },
          "100%": { opacity: 1 },
        },
      },
    },
    container: {
      center: true,
    },
    boxShadow: {
      DEFAULT: "9px 9px 30px -11px rgba(0,0,0,0.75)",
      sm: "0px 6px 15px -5px rgba(0, 0, 0, 0.71)",
    },
  },

  plugins: [require("flowbite/plugin")],
};
