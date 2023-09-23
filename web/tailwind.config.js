/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './index.html',
        './src/**/*.{vue,js,ts,jsx,tsx}'
    ],
    theme: {
        extend: {
            fontFamily: {
                'title': ['SemplicitaObra', 'sans-serif']
            },
            colors: {
                'accent': '#E32D91',
                'accentDark': '#911c5d'
            }
        },
    },
    plugins: [],
}