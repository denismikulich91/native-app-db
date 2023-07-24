<template>
    <div class="q-pl-md q-pt-md">
        <div class="text-italic text-h6 q-mb-sm text-primary">
            Project: <span class="text-weight-bolder">{{ siteName }}</span>
        </div>
        <div class="date row">
            <p class="text-italic text-h6 q-mb-sm">Latest design update: <span class="text-weight-bolder">{{ modDate }}</span></p>
            <q-icon class="q-pl-sm" name="schedule" size="md" />
        </div>
        <div class="trigramm row">
            <p class="text-italic text-subtitle2">By <span class="text-weight-bolder">{{ trigramm }}</span></p>
            <q-icon class="q-pl-sm" name="person" size="sm" />
        </div>
    </div>
    <div class="q-pa-md">
        <q-list bordered class="rounded-borders">
            <q-expansion-item expand-separator icon="tune" label="Global parameters" header-class="text-primary">
                <q-card>
                    <q-card-section>
                        <li v-for="(key, value) in globalParameters" class="q-pl-md text-primary">
                            {{ `${value}: ${key[0]} ${key[1]}` }}
                        </li>
                    </q-card-section>
                </q-card>
            </q-expansion-item>
            <q-expansion-item expand-separator icon="settings" label="Loading parameters" header-class="text-warning">
                <q-card>
                    <q-card-section>
                        <li v-for="(key, value) in loadingParameters" class="q-pl-md text-warning">
                            {{ `${value}: ${key[0]} ${key[1]}` }}
                        </li>
                    </q-card-section>
                </q-card>
            </q-expansion-item>
            <q-expansion-item expand-separator icon="settings" label="Undercut parameters" header-class="text-primary">
                <q-card>
                    <q-card-section q-pb-sm>
                        <li v-for="(key, value) in undercutParameters" class="q-pl-md text-primary">
                            {{ `${value}: ${key[0]} ${key[1]}` }}
                        </li>
                    </q-card-section>
                </q-card>
            </q-expansion-item>
        </q-list>
        <div class="totals">
            <div class="row parameters">
                <p class="text-italic text-uppercase text-body1">Totals</p>
                <q-icon class="q-pl-sm" name="bar_chart" size="sm" />
            </div>
            <li v-for="(key, value) in totals" class="q-pl-md">
                {{ `${value}: ${key[0]} ${key[1]}` }}
            </li>
            <div class="profile row q-pa-md">
                <img class="col-auto" src="../static/images/profile.jpg" alt="">
                <div class="col q-ml-md q-mt-sm text-primary">
                    {{ `- H (Tunnel heigth): ${profile.tunnel_height} m` }} <br>
                    {{ `- W (Tunnel width): ${profile.tunnel_width} m` }} <br>
                    {{ `- R (Tunnel radius): ${profile.tunnel_r} m` }}
                </div>
            </div>
        </div>
    </div>
</template>

<!-- no scope for app.vue, style defined here is global for the app -->
<style>
    .parameters{
        margin-top: 25px;
    };
    .totals{
        border: 1px;
    }
</style>

<script>
import axios from "axios";
import { widget } from "@widget-lab/3ddashboard-utils";
console.debug(widget);

export default {
    name: "App",
    components: {
  },
    data() {
        return {
            receivedData: null,
            modDate: "",
            trigramm: "",
            globalParameters: null,
            loadingParameters: null,
            undercutParameters: null,
            totals: null,
            siteName: "",
            profile: {
                tunnel_width: "",
                tunnel_height: "",
                tunnel_r: ""
            }
        };
    },
    async mounted() {
        await axios.get("http://localhost:5000/api/user/DMH5")
            .then(response => {
                this.receivedData = response.data;
                this.modDate = response.data.mod_date;
                this.trigramm = response.data.name;
                this.globalParameters = response.data.parameters.global;
                this.loadingParameters = response.data.parameters.loading;
                this.undercutParameters = response.data.parameters.undercut;
                this.totals = response.data.parameters.totals;
                this.profile = response.data.parameters.profile;
                this.siteName = response.data.parameters.site_name;
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            });
    },

    methods: {

        }
    }

</script>
