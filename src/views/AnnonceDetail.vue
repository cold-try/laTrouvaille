<template>

    <div ref="topContainer" class="container">
        <h2 class="detail-title-article is-primary">
            {{this.articleDetails.nom}}
        </h2>

        <hr>

        <div class="columns">
            <p class="dateParution" v-text="this.formatageDate(articleDetails.date)"></p>
            <p class="has-text-weight-bold" style="color:#485fc7"> • {{articleDetails.categorie.nom}}</p>
        </div>

        <figure class="image">
            <img :src="articleDetails.main_picture" class="main-picture-article" alt="Placeholder image">
        </figure>

        <div class="columns">
            <div class="column is-1"></div>
            <div class="column is-10 detail-description">
                <p>{{articleDetails.main_description}}</p>
            </div>
        </div>

        <div class="has-text-centered">
            <button class="button is-medium buyCall">Je le veux !</button>
        </div>

        <hr>

        <!-- Facultatif descriptions + pictures -->
        <div class="has-text-centered">
            <template v-if="articleDetails.second_picture">
                <figure class="image image-facultatif">
                    <img :src="articleDetails.second_picture" class="main-picture-article" alt="Placeholder image">
                </figure>
            </template>
            <template v-if="articleDetails.second_description">
                <div class="columns">
                    <div class="column is-1"></div>
                    <div class="column is-10 detail-description">
                        <p>{{articleDetails.second_description}}</p>
                    </div>
                </div>
            </template>

            <template v-if="articleDetails.third_picture">
                <figure class="image image-facultatif">
                    <img :src="articleDetails.third_picture" class="main-picture-article" alt="Placeholder image">
                </figure>
            </template>
            <template v-if="articleDetails.third_description">
                <div class="columns">
                    <div class="column is-1"></div>
                    <div class="column is-10 detail-description">
                        <p>{{articleDetails.third_description}}</p>
                    </div>
                </div>
            </template>

            <template v-if="articleDetails.fourth_picture">
                <figure class="image image-facultatif">
                    <img :src="articleDetails.fourth_picture" class="main-picture-article" alt="Placeholder image">
                </figure>
            </template>
            <template v-if="articleDetails.fourth_description">
                <div class="columns">
                    <div class="column is-1"></div>
                    <div class="column is-10 detail-description">
                        <p>{{articleDetails.fourth_description}}</p>
                    </div>
                </div>
            </template>

            <template v-if="articleDetails.fifth_picture">
                <figure class="image image-facultatif">
                    <img :src="articleDetails.fifth_picture" class="main-picture-article" alt="Placeholder image">
                </figure>
            </template>
            <template v-if="articleDetails.fifth_description">
                <div class="columns">
                    <div class="column is-1"></div>
                    <div class="column is-10 detail-description">
                        <p>{{articleDetails.fifth_description}}</p>
                    </div>
                </div>
            </template>

            <template v-if="articleDetails.sixth_picture">
                <figure class="image image-facultatif">
                    <img :src="articleDetails.sixth_picture" class="main-picture-article" alt="Placeholder image">
                </figure>
            </template>
            <template v-if="articleDetails.sixth_description">
                <div class="columns">
                    <div class="column is-1"></div>
                    <div class="column is-10 detail-description">
                        <p>{{articleDetails.sixth_description}}</p>
                    </div>
                </div>
            </template>
        </div>

        <!-- ---------------------- -->

        <div class="columns">
            <div class="column is-1"></div>
            <div class="column is-12 detail-description">
                <div class="columns">
                    <div class="column is-5 features-block">
                        <h2 class="title-details has-text-weight-bold">
                            <svg class="feature-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M14.44 18.56H9.57C9.47136 18.5588 9.37381 18.5808 9.28523 18.6243C9.19665 18.6677 9.1195 18.7313 9.06 18.81C8.99107 18.882 8.94053 18.9697 8.91268 19.0654C8.88483 19.1612 8.88048 19.2622 8.9 19.36C9.02522 20.0928 9.40559 20.7577 9.97383 21.2371C10.5421 21.7165 11.2616 21.9795 12.005 21.9795C12.7484 21.9795 13.4679 21.7165 14.0362 21.2371C14.6044 20.7577 14.9848 20.0928 15.11 19.36C15.1292 19.263 15.1257 19.1628 15.0996 19.0674C15.0736 18.9719 15.0258 18.8838 14.96 18.81C14.8974 18.7322 14.8183 18.6694 14.7283 18.6262C14.6383 18.5829 14.5398 18.5603 14.44 18.56Z" fill="#A6A6EF"/>
                                <path d="M16.17 3.48001C15.3985 2.85529 14.4967 2.41152 13.531 2.18135C12.5654 1.95118 11.5604 1.94047 10.59 2.15001C9.46012 2.39204 8.41375 2.92692 7.55582 3.70098C6.69789 4.47505 6.05858 5.46108 5.702 6.5602C5.34542 7.65932 5.28411 8.83288 5.52421 9.96317C5.76432 11.0935 6.29741 12.1408 7.07001 13C7.56268 13.5524 7.8458 14.2602 7.87001 15V15.5C7.8692 15.9555 8.01306 16.3994 8.28085 16.7679C8.54864 17.1363 8.92652 17.4102 9.36001 17.55C9.42928 17.5643 9.50073 17.5643 9.57 17.55H14.44C14.5126 17.5643 14.5874 17.5643 14.66 17.55C15.09 17.4058 15.464 17.1305 15.7294 16.7628C15.9949 16.3951 16.1385 15.9535 16.14 15.5V15C16.1505 14.2239 16.4418 13.4778 16.96 12.9C17.5449 12.2342 17.9896 11.4573 18.2673 10.6157C18.5451 9.77415 18.6502 8.88519 18.5764 8.00203C18.5027 7.11888 18.2516 6.25967 17.8381 5.47581C17.4246 4.69195 16.8573 3.99954 16.17 3.44001V3.48001ZM15.12 9.28C14.9397 9.28 14.7667 9.20836 14.6392 9.08084C14.5116 8.95331 14.44 8.78035 14.44 8.60001C14.4374 7.95369 14.1795 7.33459 13.7224 6.87757C13.2654 6.42055 12.6463 6.16264 12 6.16001C11.8197 6.16001 11.6467 6.08836 11.5192 5.96084C11.3916 5.83331 11.32 5.66035 11.32 5.48001C11.32 5.29966 11.3916 5.1267 11.5192 4.99917C11.6467 4.87165 11.8197 4.80001 12 4.80001C13.007 4.80264 13.972 5.20385 14.6841 5.91592C15.3962 6.62798 15.7974 7.59299 15.8 8.60001C15.7974 8.77955 15.7249 8.95101 15.598 9.07798C15.471 9.20495 15.2995 9.27742 15.12 9.28Z" fill="#A6A6EF"/>
                            </svg>
                            Fonctionnalités
                        </h2>
                        <p class="features">{{articleDetails.features}}</p>
                    </div>
                    <div class="column is-5">
                        <div class="last-call">
                            <p class="price-details">
                                <svg class="price-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M21.57 5.1C21.43 3.69 20.31 2.56 18.9 2.43L14.52 2.01C13.6 1.92 12.69 2.25 12.03 2.91L2.92001 12.02C2.34001 12.6 2.01 13.37 2 14.18C1.99 14.99 2.28999 15.76 2.86999 16.33L7.66 21.13C8.24 21.71 8.99999 21.99 9.76999 21.99C10.56 21.99 11.36 21.69 11.97 21.08L21.08 11.97C21.74 11.31 22.07 10.4 21.99 9.48L21.57 5.1ZM15.66 6.48C16.17 5.96 17 5.97 17.52 6.48C18.03 6.99 18.03 7.82999 17.52 8.33999C17.26 8.59999 16.92 8.72 16.59 8.72C16.25 8.72 15.91 8.59999 15.66 8.33999C15.14 7.82999 15.14 6.99 15.66 6.48Z" fill="#A6A6EF"/>
                                </svg>
                                {{articleDetails.price}} €
                            </p>
                            <button class="button is-medium buyCall">Acheter maintenant</button>
                            <p class="amz-link">Amazon.com</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'AnnonceDetail',
    created() {
        this.$store.dispatch('articleDetails', this.$route.params.pk)
        .then(() => {
            var element = this.$refs.topContainer;
            element.scrollIntoView({block: "start"});
        });
    },
    data() {
      return {
      }
    },
    computed: mapState ([
        'articleDetails'
    ]),
    components: {
    },
    methods: {
        formatageDate: function(date) {
        const months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
        'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
        const today = new Date();
        var currentYear = today.getFullYear();
        var currentDay = String(today.getDate()).padStart(2, '0');
        var currentMonth = String(today.getMonth() + 1).padStart(2, '0');

        var year = date.substring(0,4)
        var month = months[parseInt(date.substring(5,7))-1]
        var day = date.substring(8,10)

        if (currentYear == year && currentDay == day && currentMonth == date.substring(5,7)) {
          return ("Aujourd'hui")
        } else {
          if (currentYear == year) {
            return(day + ' ' + month)
          } else {
            return(day + ' ' + month + ' ' + year)
          }
        }
      },
    }
}
</script>

<style lang="scss">
    .detail-title-article {
        margin-top:5%;
        font-size:2em;
        font-weight: bold;
    }

    .dateParution {
        font-style: italic;
        margin-right:0.5%;
    }

    .main-picture-article {
        max-height: 600px;
        object-fit: contain;
        background-position: center center;
        border-radius: 20px;
    }

    .detail-description {
        margin-top:3%;
        font-size: 1.2em;
    }

    .buyCall {
        background-color: #2b783e!important;
        border-color: #2b783e!important;
        color:white!important;
        font-weight: bold;
    }

    .features {
        white-space: pre-wrap;
    }

    .feature-icon {
        width: 50px;
        margin-bottom: -1%;
    }

    .features-block {
        border-right: 0.4px solid;
        margin-right: 5%;
        border-color: #e4e4e4;
    }

    .title-details {
        font-weight: bold;
        font-size: 2em;
        margin-bottom:4%;
    }

    .price-details {
        color: #B12704;
        font-weight: bold;
        font-size: 1.5em;
        margin-top:5%;
        margin-bottom:2%;
    }

    .price-icon {
        width: 30px;
        margin-bottom:-1.2%;
    }

    .amz-link {
        color:grey;
        font-size: 0.7em;
        margin-top:2%;
    }

    .last-call {
        padding: 3%;
    }

    .image-facultatif {
        width: 60%;
        margin-left: auto;
        margin-right: auto;
    }
</style>