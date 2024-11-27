module.exports = {
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": [
        "eslint:recommended",
        "plugin:vue/essential"
    ],
    "parserOptions": {
        "ecmaVersion": 12,
        "sourceType": "module"
    },
    "plugins": [
        "vue"
    ],
    "rules": {
    }
};


module.exports = {
    extends: [
      'plugin:vue/vue3-essential', // sau alte configurări în funcție de proiectul tău
    ],
    rules: {
      'vue/multi-word-component-names': 'off', // Dezactivează regula pentru toate componentele
    },
  };