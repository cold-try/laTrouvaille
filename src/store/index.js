import { createStore } from 'vuex'
import axios from 'axios' 

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;
const instance = axios.create({
  withCredentials: true,
  baseURL: process.env.API_URL
})

export default createStore({
  state: {
    completionResults: [],
    articles: [],
    totalPages: 1,
    pageLink: {},
    currentPage: 1,
    articleDetails: [],
    relatedArticles: [],
    comments: [],
    categories: [],
    fromCategory: false,
    categoryId: null,
    loading: false,
  },

  mutations: {
    articles(state, data) {
      state.articles = data.results;
      state.totalPages = data.total_pages;
      state.pageLink = data.links;
      state.currentPage = data.currentPage;
    },

    articleDetails(state, data) {
      state.articleDetails = data;
    },

    relatedArticles(state, data) {
      state.relatedArticles = data;
    },

    getCategories(state, data) {
      state.categories = data;
    },

    origin(state, data) {
      state.fromCategory = data;
    },

    categoryId(state, data) {
      state.categoryId = data;
    },

    comments(state, data) {
      state.comments = data;
    },

    loadingOn(state) {
      state.loading = true;
    },

    loadingStop(state) {
      state.loading = false;
    },

    completionResults(state, data) {
      state.completionResults = data;
    },

    resetCompletionResults(state) {
      state.completionResults = [];
    }
  },

  actions: {
    lastEntries({commit}, infoPage) {
      commit('loadingOn');
      if(!infoPage) {
        return new Promise((resolve) => {
          instance.get('/core/core/last_entries/')
          .then(response => {
            commit('articles', response.data.articles);
            commit('origin', response.data.fromCategory);
            commit('loadingStop');
            resolve();
          })
        })
      } else {
        // Page numérotée //
        if(typeof(infoPage) == 'number') {
          return new Promise((resolve) => {
            instance.get('/core/core/last_entries/?p='+infoPage)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('loadingStop');
              resolve();
            })
          })
        } else {
          // Page suivante-précedente //
          return new Promise((resolve) => {
            instance.get(infoPage)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('loadingStop');
              resolve();
            })
          })
        }
      }
    },

    perCategories({commit}, data) {
      commit('loadingOn');
      if(!data.infoPage) {
        return new Promise((resolve) => {
          instance.get('/core/core/per_categories/'+data.id)
          .then(response => {
            commit('articles', response.data.articles);
            commit('origin', response.data.fromCategory);
            commit('categoryId', response.data.categoryId);
            commit('loadingStop');
            resolve();
          })
        })
      } else {
        // Page numérotée //
        if(typeof(data.infoPage) == 'number') {
          return new Promise((resolve) => {
            instance.get('/core/core/per_categories/'+data.id+'/?p='+data.infoPage)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('categoryId', response.data.categoryId);
              commit('loadingStop');
              resolve();
            })
          })
        } else {
          // Page suivante-précedente //
          return new Promise((resolve) => {
            instance.get(data)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('categoryId', response.data.categoryId);
              commit('loadingStop');
              resolve();
            })
          })
        }
      }
    },

    articleDetails({commit}, data) {
      commit('loadingOn');
      return new Promise((resolve) => {
        instance.get('/core/core/article_details/'+data)
        .then(response => {
          commit('articleDetails', response.data.articleDetails);
          commit('relatedArticles', response.data.relatedArticles);
          commit('comments', response.data.comments);
          commit('loadingStop');
          resolve();
        })
      })
    },

    sendCommentary({commit}, data) {
      return new Promise((resolve) => {
        instance.post('/core/core/send_commentary/', {
          id: data.id, 
          commentAuthor: data.commentAuthor, 
          commentContent: data.commentContent,
          commentEmail: data.commentEmail, 
          commentWebsite: data.commentWebsite
        })
        .then(response => {
          commit('comments', response.data.comments);
          resolve();
        })
      })
    },

    getCategories({commit}) {
      return new Promise((resolve) => {
        instance.get('/core/core/get_categories/')
        .then(response => {
          commit('getCategories', response.data.getCategories);
          resolve();
        })
      })
    },

    getBestOf({commit}, data) {
      commit('loadingOn');
      if(!data) {
        return new Promise((resolve) => {
          instance.get('/core/core/get_bestof/')
          .then(response => {
            commit('articles', response.data.articles);
            commit('origin', 'Meilleur de 2022');
            commit('loadingStop');
            resolve();
          })
        })
      } else {
        // Page numérotée //
        if(typeof(data) == 'number') {
          return new Promise((resolve) => {
            instance.get('/core/core/get_bestof/?p='+data)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('loadingStop');
              resolve();
            })
          })
        } else {
          // Page suivante-précedente //
          return new Promise((resolve) => {
            instance.get(data)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('loadingStop');
              resolve();
            })
          })
        }
      }
    },

    getSelection({commit}, data) {
      commit('loadingOn');
      if(!data) {
        return new Promise((resolve) => {
          instance.get('/core/core/get_selection/')
          .then(response => {
            commit('articles', response.data.articles);
            commit('origin', 'Notre sélection');
            commit('loadingStop');
            resolve();
          })
        })
      } else {
        // Page numérotée //
        if(typeof(data) == 'number') {
          return new Promise((resolve) => {
            instance.get('/core/core/get_selection/?p='+data)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('loadingStop');
              resolve();
            })
          })
        } else {
          // Page suivante-précedente //
          return new Promise((resolve) => {
            instance.get(data)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory);
              commit('loadingStop');
              resolve();
            })
          })
        }
      }
    },

    // Input search, navbar //
    inputSearchCompletion({ commit }, data) {
      instance.post('/core/core/input-completion/', {
        entries: data
      })
      .then(response => {
        commit('completionResults', response.data.completions);
      })
    },

    resetSearchCompletion({ commit }) {
      commit('resetCompletionResults');
    },

  },

  modules: {
  }
})
