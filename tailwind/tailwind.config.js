/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../**/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        base: "'Urbanist'"
      },
      colors: {
         "dark-10": "#1C212D",
         "dark-20": "#8E99A3",
         "dark-30": "#121724",
         "dark-40": "#B5BDC3",
        "yellow-10": "#FFD831",
        "green-10": "#233736",
        "green-20": "#346764",
         "green-50": "#346764",
      },
      backgroundColor: {
        "dark-10": "#1C212D",
        "yellow-10": "#FFD831",
        "grey-10": "#F3F6F9",
         "green-20": "#346764",
          "green-50": "#346764"
      },
      borderColor: {
        "grey-100": "#EAEFF4",
         "green-50": "#346764"
      }
    },
  },
  plugins: [],
}
