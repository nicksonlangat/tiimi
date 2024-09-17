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
        "yellow-10": "#FFD831"
      },
      backgroundColor: {
        "dark-10": "#1C212D",
        "yellow-10": "#FFD831",
        "grey-10": "#F3F6F9"
      }
    },
  },
  plugins: [],
}
