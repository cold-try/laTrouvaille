<template>


  <div @click="unFocus()" ref="articlesTop" class="container">

    <h2 class="title-top has-text-weight-bold">
      <template v-if="this.fromCategory">
        <template v-if="this.fromCategory == 'Notre sélection'">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M11.13 11.17L14.25 9.76L12.87 12.83L9.72 14.32L11.13 11.17Z" fill="#A6A6EF"/>
              <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM15.7 10.17L14.19 13.49C14.05 13.8 13.8 14.05 13.49 14.19L10.17 15.7C9.98 15.79 9.78 15.83 9.58 15.83C9.21 15.83 8.86 15.69 8.58 15.42C8.16 15 8.05 14.37 8.3 13.83L9.81 10.51C9.95 10.2 10.2 9.95 10.51 9.81L13.83 8.3C14.37 8.05 15 8.16 15.42 8.58C15.84 9 15.95 9.63 15.7 10.17Z" fill="#A6A6EF"/>
          </svg>
        </template>

        <template v-else-if="this.fromCategory == 'Meilleur de 2022'">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19.3 4.05H17.92V2.75C17.9213 2.65114 17.9029 2.55301 17.8656 2.4614C17.8284 2.3698 17.7732 2.28659 17.7033 2.21667C17.6334 2.14676 17.5502 2.09156 17.4586 2.05435C17.367 2.01714 17.2689 1.99865 17.17 2H6.88999C6.69108 2 6.50031 2.07902 6.35966 2.21967C6.21901 2.36032 6.13999 2.55109 6.13999 2.75V4.05H4.70999C4.25541 4.03377 3.81291 4.19826 3.47932 4.50749C3.14573 4.81672 2.94822 5.2455 2.92999 5.7V8.93C2.93116 9.15616 2.98086 9.37944 3.07575 9.58473C3.17063 9.79003 3.30849 9.97257 3.47999 10.12L7.14999 13.38C7.62118 14.053 8.23252 14.6161 8.942 15.0304C9.65149 15.4447 10.4423 15.7004 11.26 15.78V17.39H8.81999C8.37939 17.3929 7.95553 17.5592 7.63042 17.8566C7.30532 18.154 7.10206 18.5614 7.05999 19L6.90999 20C6.8768 20.2521 6.898 20.5084 6.97217 20.7516C7.04635 20.9948 7.17177 21.2193 7.33999 21.41C7.50597 21.5985 7.71078 21.7488 7.94036 21.8507C8.16995 21.9525 8.41886 22.0035 8.66999 22H15.39C15.6418 21.9991 15.8905 21.9448 16.1198 21.8407C16.349 21.7365 16.5536 21.585 16.7199 21.3959C16.8863 21.2069 17.0106 20.9847 17.0847 20.7441C17.1589 20.5035 17.1811 20.2499 17.15 20L17 19C16.94 18.5749 16.7293 18.1855 16.4063 17.9028C16.0832 17.6202 15.6693 17.463 15.24 17.46H12.78V15.8C13.6289 15.7205 14.4491 15.4509 15.1796 15.0112C15.9102 14.5715 16.5323 13.973 17 13.26L20.52 10.13C20.6913 9.9802 20.8288 9.7958 20.9236 9.58896C21.0184 9.38212 21.0683 9.15753 21.07 8.93V5.7C21.0623 5.4754 21.0103 5.25452 20.9171 5.05C20.824 4.84549 20.6914 4.66135 20.527 4.5081C20.3626 4.35486 20.1696 4.23552 19.9591 4.15692C19.7486 4.07831 19.5246 4.04198 19.3 4.05ZM4.42999 8.93V5.7C4.42999 5.65 4.53999 5.55 4.70999 5.55H6.13999V10.14C6.13999 10.26 6.13999 10.37 6.13999 10.48L4.42999 8.93ZM14.43 8.53L13.77 9.18L13.92 10.09C13.9447 10.2281 13.9306 10.3703 13.8794 10.5009C13.8283 10.6315 13.7419 10.7454 13.63 10.83C13.5065 10.9278 13.3569 10.9869 13.2 11C13.081 10.9986 12.9641 10.9676 12.86 10.91L12 10.45L11.18 10.88C11.0568 10.9462 10.9175 10.9765 10.7779 10.9677C10.6383 10.9589 10.5039 10.9112 10.39 10.83C10.2763 10.7466 10.188 10.6333 10.135 10.5026C10.082 10.3719 10.0664 10.229 10.09 10.09L10.25 9.18L9.57999 8.53C9.47948 8.43206 9.40846 8.30789 9.37501 8.17159C9.34157 8.0353 9.34703 7.89235 9.39078 7.75901C9.43454 7.62567 9.51482 7.50727 9.62252 7.41729C9.73021 7.32731 9.86099 7.26935 9.99999 7.25L11 7.11L11.41 6.28C11.4805 6.16411 11.5796 6.06832 11.6978 6.00185C11.816 5.93537 11.9494 5.90046 12.085 5.90046C12.2206 5.90046 12.354 5.93537 12.4722 6.00185C12.5904 6.06832 12.6895 6.16411 12.76 6.28L13.17 7.11L14.09 7.25C14.2275 7.27103 14.3564 7.32986 14.4623 7.41992C14.5683 7.50998 14.6471 7.62773 14.69 7.76C14.7288 7.89781 14.7267 8.0439 14.6841 8.18057C14.6415 8.31724 14.5602 8.43862 14.45 8.53H14.43ZM15.23 18.91C15.2967 18.9096 15.3612 18.9339 15.411 18.9782C15.4609 19.0225 15.4926 19.0837 15.5 19.15L15.65 20.15C15.654 20.1895 15.6499 20.2294 15.6378 20.2673C15.6258 20.3051 15.6061 20.3401 15.58 20.37C15.5552 20.4018 15.5232 20.4274 15.4868 20.4448C15.4503 20.4621 15.4104 20.4708 15.37 20.47H8.66999C8.63104 20.4708 8.59248 20.4621 8.55764 20.4447C8.52279 20.4273 8.49271 20.4016 8.46999 20.37C8.43997 20.3428 8.41768 20.3081 8.40539 20.2694C8.3931 20.2308 8.39124 20.1896 8.39999 20.15L8.53999 19.15C8.55158 19.0837 8.58585 19.0235 8.63693 18.9798C8.68801 18.936 8.75273 18.9113 8.81999 18.91H15.23ZM19.52 9L17.91 10.44C17.91 10.34 17.91 10.24 17.91 10.14V5.55H19.3C19.47 5.55 19.57 5.65 19.57 5.7L19.52 9Z" fill="#A6A6EF"/>
          </svg>
        </template>

        <template v-else>
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3.78003 12.75H6.11002V20.22C6.11002 21.2 6.91005 22 7.89005 22H8.92004C9.90004 22 10.69 21.2 10.69 20.22V12.75H17.48C17.69 12.75 17.9 12.66 18.04 12.5L20.78 9.41C21.04 9.13 21.04 8.7 20.78 8.42L18.04 5.33C17.9 5.17 17.69 5.08 17.48 5.08H10.69V3.78C10.69 2.8 9.90004 2 8.92004 2H7.89005C6.91005 2 6.11002 2.8 6.11002 3.78V5.08H3.78003C3.36003 5.08 3.03003 5.42 3.03003 5.83V12C3.03003 12.41 3.36003 12.75 3.78003 12.75ZM7.61002 3.78C7.61002 3.63 7.74005 3.5 7.89005 3.5H8.92004C9.07004 3.5 9.19003 3.63 9.19003 3.78V5.08H7.61002V3.78ZM7.61002 12.75H9.19003V20.22C9.19003 20.37 9.07004 20.5 8.92004 20.5H7.89005C7.74005 20.5 7.61002 20.37 7.61002 20.22V12.75Z" fill="#A6A6EF"/>
          </svg>
        </template>
    
        <span class="accueil-title">{{this.fromCategory}}</span>
      </template>

      <template v-else>
        <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19.19 5.03H16.11C15.7 5.03 15.36 5.37 15.36 5.78V8.11H11.29C11.54 7.54 11.72 6.95 11.72 6.4C11.72 4.57 10.23 3.08 8.39999 3.08C6.56999 3.08 5.08 4.57 5.08 6.4C5.08 6.94 5.26 7.54 5.52 8.11H4.81C3.26 8.11 2 9.37 2 10.92V18.11C2 19.66 3.26 20.92 4.81 20.92H19.19C20.74 20.92 22 19.66 22 18.11V7.84C22 6.29 20.74 5.03 19.19 5.03ZM8.39999 5.6C8.88999 5.6 9.28999 6 9.28999 6.49C9.28999 6.98 8.88999 7.37 8.39999 7.37C7.90999 7.37 7.52 6.98 7.52 6.49C7.52 6 7.90999 5.6 8.39999 5.6ZM10.22 19.42H4.81C4.09 19.42 3.5 18.83 3.5 18.11V14.75H6.86C7.04 14.75 7.14 14.85 7.14 14.89C7.14 15.78 7.94 16.52 8.92 16.52H9.94C10.13 16.52 10.22 16.62 10.22 16.65V19.42ZM19.19 19.42H11.72V16.65C11.72 15.75 10.92 15.02 9.94 15.02H8.92C8.74 15.02 8.64 14.92 8.64 14.89C8.64 13.99 7.84 13.25 6.86 13.25H3.5V10.92C3.5 10.2 4.09 9.61 4.81 9.61H6.35001C6.90001 10.45 7.46999 11.12 7.67999 11.35C7.85999 11.55 8.12999 11.67 8.39999 11.67C8.67999 11.67 8.95001 11.55 9.13 11.35C9.33 11.12 9.91001 10.45 10.46 9.61H15.36V16.06C15.36 16.47 15.7 16.81 16.11 16.81H19.19C19.91 16.81 20.5 17.4 20.5 18.11C20.5 18.83 19.91 19.42 19.19 19.42Z" fill="#A6A6EF"/>
        </svg>
        <span class="accueil-title">Nos dernières trouvailles</span>
      </template>
    </h2>

    <hr>
    
    <div class="columns is-12 articles-container">
      <template v-if="this.loading">
          <div id="loading-accueil-gif" class="column has-text-centered">
              <img :src="loadingSvg" />
          </div>
      </template>

      <template v-else>
        <template v-if="this.articles.length > 0">
          <template v-for="(article, index) in this.articles" :key="index">

            <div 
            @mouseenter="displaySocialMediaBloc(article.id)" 
            @mouseleave="hideSocialMediaBloc(article.id)"
            class="column is-4 article-bloc">
              <div class="card">
                <div class="card-image preview-article-div">
                  <figure class="image">
                    <div :ref="'socialMediaBloc'+article.id" class="social-media is-hidden is-hidden-mobile">
                      <a @click="socialShare('Twitter', article.id)">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M17.14 2H6.86C4.18 2 2 4.18 2 6.86V17.14C2 19.82 4.18 22 6.86 22H17.14C19.82 22 22 19.82 22 17.14V6.86C22 4.18 19.82 2 17.14 2ZM16.79 8.87C17.41 11.31 16.72 13.87 14.96 15.44C12.7 17.46 9.03 17.55 6.34 15.45C6.54 15.48 6.72001 15.49 6.88 15.48C8.15 15.43 9.01999 14.42 9.28999 14.08C8.81999 13.67 8.09 12.95 7.58 11.84C6.86 10.3 6.93 8.85 7.05 8.03C7.08 7.87 7.27999 7.81 7.39999 7.94C7.76999 8.36 8.37 8.93 9.25 9.34C10.2 9.78 11.06 9.86 11.55 9.86C11.52 8.67 12.23 7.6 13.3 7.19C14.24 6.82 15.33 7.03 16.1 7.73C16.62 7.71 17.14 7.69999 17.66 7.67999C17.37 8.07999 17.08 8.47 16.79 8.87Z" fill="rgb(29, 155, 240)"/>
                        </svg>
                      </a>

                      <a @click="socialShare('Facebook', article.id)"
                      style="margin-top:-25%" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M22 6.86V17.14C22 19.82 19.82 22 17.14 22H15.79V15.41C15.79 15.13 16.02 14.91 16.29 14.91H17.76C18.01 14.91 18.22 14.72 18.25 14.47L18.48 12.75C18.52 12.45 18.29 12.18 17.99 12.18H16.29C16.02 12.18 15.79 11.96 15.79 11.68V10.46C15.79 10.06 15.87 9.74 16.03 9.5C16.23 9.26 16.59 9.14 17.11 9.14H18.06C18.33 9.14 18.56 8.91 18.56 8.64V7.18C18.56 6.92 18.37 6.7 18.12 6.68C17.64 6.63 17.08 6.61 16.47 6.61C15.39 6.61 14.55 6.93 13.91 7.57C13.27 8.21 12.99 9.06 12.99 10.18V11.68C12.99 11.96 12.76 12.18 12.49 12.18H11.04C10.77 12.18 10.54 12.41 10.54 12.68V14.41C10.54 14.68 10.77 14.91 11.04 14.91H12.49C12.76 14.91 12.99 15.13 12.99 15.41V22H6.86C4.18 22 2 19.82 2 17.14V6.86C2 4.18 4.18 2 6.86 2H17.14C19.82 2 22 4.18 22 6.86Z" fill="#3b5998"/>
                        </svg>
                      </a>

                      <a @click="socialShare('Pinterest', article.id)"
                      style="margin-top:-25%" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM10.48 20.98C10.39 21.31 10.09 21.53 9.76001 21.53C9.69001 21.53 9.63 21.53 9.56 21.51C9.16 21.4 8.92 20.99 9.03 20.59L9.17999 20.02L11.28 12.14C11.38 11.75 11.79 11.5 12.19 11.61C12.59 11.72 12.83 12.13 12.73 12.53L11.96 15.44C12.04 15.44 12.13 15.47 12.21 15.5C12.47 15.61 12.73 15.67 12.99 15.67H13.03C14.35 15.67 15.8 14.24 16.09 12.65C16.21 11.94 16.12 11.28 15.82 10.69C15.12 9.31 13.47 8.69 12.24 8.69C10.8 8.69 9.63 9.14 8.87 9.98C8.25 10.66 7.95999 11.39 8.01999 12.16C8.07999 13.01 8.56 13.63 8.84 13.92C9.12 14.22 9.11 14.69 8.81 14.98C8.51 15.27 8.04 15.26 7.75 14.96C7.33 14.52 6.61999 13.59 6.51999 12.26C6.45999 11.45 6.63 10.22 7.75 8.97C8.79 7.82 10.39 7.19 12.24 7.19C13.97 7.19 16.16 8.06 17.16 10C17.47 10.61 17.79 11.61 17.56 12.91C17.2 14.99 15.29 17.17 13.03 17.17H12.95C12.5 17.16 12.05 17.06 11.61 16.87C11.6 16.86 11.59 16.86 11.58 16.85L10.64 20.39L10.48 20.98Z" fill="#e60023"/>
                        </svg>
                      </a>
                    </div>

                    <div class="social-media is-hidden-tablet">
                      <a @click="socialShare('Twitter', article.id)">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M17.14 2H6.86C4.18 2 2 4.18 2 6.86V17.14C2 19.82 4.18 22 6.86 22H17.14C19.82 22 22 19.82 22 17.14V6.86C22 4.18 19.82 2 17.14 2ZM16.79 8.87C17.41 11.31 16.72 13.87 14.96 15.44C12.7 17.46 9.03 17.55 6.34 15.45C6.54 15.48 6.72001 15.49 6.88 15.48C8.15 15.43 9.01999 14.42 9.28999 14.08C8.81999 13.67 8.09 12.95 7.58 11.84C6.86 10.3 6.93 8.85 7.05 8.03C7.08 7.87 7.27999 7.81 7.39999 7.94C7.76999 8.36 8.37 8.93 9.25 9.34C10.2 9.78 11.06 9.86 11.55 9.86C11.52 8.67 12.23 7.6 13.3 7.19C14.24 6.82 15.33 7.03 16.1 7.73C16.62 7.71 17.14 7.69999 17.66 7.67999C17.37 8.07999 17.08 8.47 16.79 8.87Z" fill="rgb(29, 155, 240)"/>
                        </svg>
                      </a>

                      <a @click="socialShare('Facebook', article.id)"
                      style="margin-top:-25%" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M22 6.86V17.14C22 19.82 19.82 22 17.14 22H15.79V15.41C15.79 15.13 16.02 14.91 16.29 14.91H17.76C18.01 14.91 18.22 14.72 18.25 14.47L18.48 12.75C18.52 12.45 18.29 12.18 17.99 12.18H16.29C16.02 12.18 15.79 11.96 15.79 11.68V10.46C15.79 10.06 15.87 9.74 16.03 9.5C16.23 9.26 16.59 9.14 17.11 9.14H18.06C18.33 9.14 18.56 8.91 18.56 8.64V7.18C18.56 6.92 18.37 6.7 18.12 6.68C17.64 6.63 17.08 6.61 16.47 6.61C15.39 6.61 14.55 6.93 13.91 7.57C13.27 8.21 12.99 9.06 12.99 10.18V11.68C12.99 11.96 12.76 12.18 12.49 12.18H11.04C10.77 12.18 10.54 12.41 10.54 12.68V14.41C10.54 14.68 10.77 14.91 11.04 14.91H12.49C12.76 14.91 12.99 15.13 12.99 15.41V22H6.86C4.18 22 2 19.82 2 17.14V6.86C2 4.18 4.18 2 6.86 2H17.14C19.82 2 22 4.18 22 6.86Z" fill="#3b5998"/>
                        </svg>
                      </a>

                      <a @click="socialShare('Pinterest', article.id)"
                      style="margin-top:-25%" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM10.48 20.98C10.39 21.31 10.09 21.53 9.76001 21.53C9.69001 21.53 9.63 21.53 9.56 21.51C9.16 21.4 8.92 20.99 9.03 20.59L9.17999 20.02L11.28 12.14C11.38 11.75 11.79 11.5 12.19 11.61C12.59 11.72 12.83 12.13 12.73 12.53L11.96 15.44C12.04 15.44 12.13 15.47 12.21 15.5C12.47 15.61 12.73 15.67 12.99 15.67H13.03C14.35 15.67 15.8 14.24 16.09 12.65C16.21 11.94 16.12 11.28 15.82 10.69C15.12 9.31 13.47 8.69 12.24 8.69C10.8 8.69 9.63 9.14 8.87 9.98C8.25 10.66 7.95999 11.39 8.01999 12.16C8.07999 13.01 8.56 13.63 8.84 13.92C9.12 14.22 9.11 14.69 8.81 14.98C8.51 15.27 8.04 15.26 7.75 14.96C7.33 14.52 6.61999 13.59 6.51999 12.26C6.45999 11.45 6.63 10.22 7.75 8.97C8.79 7.82 10.39 7.19 12.24 7.19C13.97 7.19 16.16 8.06 17.16 10C17.47 10.61 17.79 11.61 17.56 12.91C17.2 14.99 15.29 17.17 13.03 17.17H12.95C12.5 17.16 12.05 17.06 11.61 16.87C11.6 16.86 11.59 16.86 11.58 16.85L10.64 20.39L10.48 20.98Z" fill="#e60023"/>
                        </svg>
                      </a>
                    </div>
                    <img @click="goToDetails(article.id)" :src="article.main_picture" class="preview-article" alt="Placeholder image">
                  </figure>
                </div>

                <div class="card-content content-article-div">
                  <div style="cursor:pointer" @click="goToDetails(article.id)">
                    <p class="title is-4">{{article.nom}}</p>

                    <div class="content description-article">
                      {{article.main_description}}
                      <br>
                    </div>
                  </div>

                  <div>
                    <template v-if="article.price">
                      <div class="price-block">
                        <p class="price">{{article.price}} €</p>
                      </div>

                      <div class="is-hidden-tablet">
                        <button @click="goToDetails(article.id)" class="button buy-block-button is-default">J'ACHETE</button>
                      </div>

                      <div class="is-hidden-mobile">
                        <button @click="goToDetails(article.id)" class="button buy-block-button">J'ACHETE</button>
                      </div>
                    </template>

                    <template v-else>
                      <button @click="goToDetails(article.id)" class="button more-block">Lire plus +</button>
                    </template>
                  </div>

                </div>
              </div>
            </div>

          </template>

          <template v-if="this.totalPages > 1">
            <div id="pagination" class="container column is-12">
              <nav class="pagination is-rounded is-centered" role="navigation" aria-label="pagination">
                <a v-if="pageLink.previous" class="pagination-previous is-hidden-mobile" 
                @click="loadNewPage(pageLink.previous)">
                  Précedent
                </a>
                <a v-else class="pagination-previous is-hidden-mobile" disabled>Précedent</a>
                <ul class="pagination-list">
                  <li>
                    <a class="pagination-link" aria-label="Goto page 1" 
                    v-if="currentPage==1"
                    disabled>
                      1
                    </a>
                    <a class="pagination-link" aria-label="Goto page 1" v-else
                    @click="loadNewPage(1)">
                      1
                    </a>
                  </li>
                  <li><span class="pagination-ellipsis">&hellip;</span></li>
                  <li v-if="currentPage==1"><a class="pagination-link" disabled>1</a></li>
                  <li v-else>
                    <a class="pagination-link" v-text="currentPage - 1" 
                    @click="loadNewPage(currentPage - 1)">
                    </a>
                  </li>
                  <li><a class="pagination-link is-current" aria-current="page">{{currentPage}}</a></li>
                  <li v-if="pageLink.next">
                    <a class="pagination-link" v-text="currentPage + 1" 
                    @click="loadNewPage(currentPage + 1)">
                    </a>
                  </li>
                  <li v-else><a class="pagination-link" v-text="currentPage + 1" disabled></a></li>
                  <li><span class="pagination-ellipsis">&hellip;</span></li>
                  <li>
                    <a class="pagination-link" 
                    v-if="this.totalPages==currentPage"
                    disabled>
                      {{totalPages}}
                    </a>
                    <a class="pagination-link" 
                    v-else
                    @click="loadNewPage(this.totalPages)">
                      {{totalPages}}
                    </a>
                  </li>
                </ul>
                <a v-if="pageLink.next" class="pagination-next is-hidden-mobile" 
                @click="loadNewPage(pageLink.next)">
                  Suivant
                </a>
                <a v-else class="pagination-next is-hidden-mobile" disabled>Suivant</a>
              </nav>
            </div>
          </template>

        </template>
      </template>
    </div>

  </div>



</template>

<script>
// @ is an alias to /src
import { mapState } from 'vuex';

export default {
  name: 'Accueil',
  created() {
    if (!this.$route.params.isFromThread) {
      if (!this.fromCategory) {
        this.$store.dispatch('lastEntries');
      }
    }
  },
  data() {
    return {
      loadingSvg: require('../assets/svg/loading.gif')
    }
  },
  computed: mapState([
    'articles',
    'totalPages',
    'pageLink',
    'currentPage',
    'fromCategory',
    'categoryId',
    'loading'
  ]),
  components: {
  },
  methods: {
    goToDetails(pk) {
      this.$router.push({ name: 'AnnonceDetail', params: {pk: pk} });
    },

    loadNewPage(dataPage) {
      if (this.fromCategory) {
        if(typeof(dataPage) == 'number') {
          if (this.fromCategory == 'Notre sélection') {
            this.$store.dispatch('getSelection', dataPage);
          } else if (this.fromCategory == 'Meilleur de 2022') {
            this.$store.dispatch('getBestOf', dataPage);
          } else {
            this.$store.dispatch('perCategories', {'id':this.categoryId, infoPage:dataPage});
          }
        } else {
          this.$store.dispatch('lastEntries', dataPage);
        }
      } else {
        this.$store.dispatch('lastEntries', dataPage);
      }
      this.goTop();
    }, 

    goTop() {
      var element = this.$refs.articlesTop;
      element.scrollIntoView({block: "start"}); 
    },

    displaySocialMediaBloc(id) {
      var targetedElement = 'socialMediaBloc' + id;
      this.$refs[targetedElement][0].className = 'social-media is-hidden-mobile anim-enter';
    },

    hideSocialMediaBloc(id) {
      var targetedElement = 'socialMediaBloc' + id;
      this.$refs[targetedElement][0].className = 'social-media is-hidden-mobile anim-exit';
    },

    socialShare(rs, id) {
      var link;
      var windowHeight = 650;
      var windowWidth = 670;
      var left = (screen.width - windowHeight) / 2;
      var top = (screen.height - windowWidth) / 4;

      if (rs == 'Twitter') {
        link = "https://twitter.com/share?url=http%3A%2F%2F127.0.0.1%3A8000%2F%23%2Fannonce_detail%2F"+id;
      } else if (rs == 'Facebook') {
        link = "https://www.facebook.com/sharer.php?u=http%3A%2F%2F127.0.0.1%3A8000%2F%23%2Fannonce_detail%2F"+id;
      } else {
        link = "https://pinterest.com/pin/create/button/?url=http%3A%2F%2F127.0.0.1%3A8000%2F%23%2Fannonce_detail%2F"+id;
      }

      window.open(link, '_blank', 'location=yes, resizable=yes, scrollbars=yes, height='+windowHeight+',width='+windowWidth+', top='+ top + ', left=' + left);
    },

    unFocus() {
      this.$store.dispatch('resetSearchCompletion');
    }
  }
}
</script>

<style lang="scss">

  @font-face {
    font-family: "leagueSpartan";
    src: url("../../public/fonts/LeagueSpartan-Bold.otf");
  }

  #loading-accueil-gif {
    margin-top:5%;
    margin-bottom:10%;
  }

  #loading-accueil-gif img {
    width:120px;
  }

  .title-top {
    font-size:1.7em;
    margin-top:2%;
    margin-bottom:2%;
  }

  .title-icon {
    margin-bottom:-0.9%;
    width: 55px;
  }

  .articles-container {
    flex-wrap: wrap;
  }

  .preview-article-div {
    height:430px;
  }

  .preview-article {
    object-fit: cover;
    cursor: pointer;
    height: 430px!important;
  }

  .content-article-div {
    height: 275px;
  }

  .description-article {
    position:relative;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: pre-wrap;
    height: 130px;
  }

  .description-article::before {
    content: " ";
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0px;
    height: 55px;
    background: linear-gradient(to bottom,  rgba(255,255,255,.5) 0%,rgba(255,255,255,1) 100%); 
  }

  .buy-block-button {
    position: absolute!important;
    bottom: 0px;
    right: 0;
    background-color:#2b783e!important;
    border-color: #2b783e!important;
    color:white!important;
    font-weight: bold;
  }

  .price-block {
    position: absolute!important;
    bottom: 0px;
    left: 0;
    background-color:#fcb900;
    padding:1%;
    padding-left:3%;
    padding-right:3%;
    font-size:1.1em;
    border-radius: 0.25rem;
  }

  .more-block {
    position: absolute!important;
    bottom: 0px;
    right: 0;
    padding:1%;
    padding-left:3%;
    padding-right:3%;
    font-size:1.1em;
    border-radius: 0.25rem;
  }

  .more {
    color:white;
    font-weight: bold!important;
  }

  #pagination {
    margin-top:5%;
  }

  .is-current {
    background-color:#A6A6EF!important;
    border-color: #A6A6EF!important;
  }

  .social-media {
    position: absolute;
    display: grid;
    right: 10px;
    top: 7px;
    font-size: 2em;
    z-index:999;
  }

  .social-media svg{
    width: 50px;
    height: 50px;
  }

  .anim-enter {
    animation: moveToLeft 200ms ease-in-out;
  }
  
  .anim-exit {
    display: none;
  }

  @keyframes moveToLeft {
    0% {
        transform: translateX(14%);
    }
    25% {
        transform: translateX(11%);
    }
    50%{
      transform: translateX(8%);
    }
    25%{
      transform: translateX(4%);
    }
    100% {
        transform: translateX(0%);
    }
  }

  // -- MOBILE -- // 

  @media only screen and (max-width:768px) {
    .article-bloc {
      margin-left: 2%!important;
      margin-right: 2%!important;
    }

    .accueil-title {
      font-size:0.85em;
    }

    .title-icon {
      margin-bottom:-2.1%;
      width: 40px;
      margin-left:2%;
      margin-right:2%;
    }

    .description-article {
      height: 130px;
    }

    .card {
      margin-left: 2%;
      margin-right: 2%;
    }
  }

  @media only screen and (max-width: 350px) {
    .accueil-title {
      font-size:0.70em;
    }

    .title-icon {
      width:40px;
      margin-bottom:-2.5%;
    }

    .description-article {
      height: 138px;
    }

    .title {
      font-size: 1.3em!important;
    }
  }
  
</style>
