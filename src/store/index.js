import { createStore } from 'vuex'
import axios from 'axios' 

const instance = axios.create({
  withCredentials: true,
  baseURL: process.env.API_URL
})

export default createStore({
  state: {
    articles: [],
    totalPages: 1,
    pageLink: {},
    currentPage: 1,
    articleDetails: [],
    categories: [],
    fromCategory: false,
    categoryId: null,
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

    getCategories(state, data) {
      state.categories = data;
    },

    origin(state, data) {
      state.fromCategory = data;
    },

    categoryId(state, data) {
      state.categoryId = data;
    }
  },

  actions: {
    lastEntries({commit}, infoPage) {
      if(!infoPage) {
        return new Promise((resolve) => {
          instance.get('/core/core/last_entries/')
          .then(response => {
            commit('articles', response.data.articles);
            commit('origin', response.data.fromCategory)
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
              commit('origin', response.data.fromCategory)
              resolve();
            })
          })
        } else {
          // Page suivante-précedente //
          return new Promise((resolve) => {
            instance.get(infoPage)
            .then(response => {
              commit('articles', response.data.articles);
              commit('origin', response.data.fromCategory)
              resolve();
            })
          })
        }
      }
    },

    perCategories({commit}, data) {
      if(!data.infoPage) {
        return new Promise((resolve) => {
          instance.get('/core/core/per_categories/'+data.id)
          .then(response => {
            commit('articles', response.data.articles);
            commit('origin', response.data.fromCategory);
            commit('categoryId', response.data.categoryId);
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
              resolve();
            })
          })
        }
      }
    },

    articleDetails({commit}, data) {
      return new Promise((resolve) => {
        instance.get('/core/core/article_details/'+data)
        .then(response => {
          commit('articleDetails', response.data.articleDetails);
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
  },

  modules: {
  }
})
