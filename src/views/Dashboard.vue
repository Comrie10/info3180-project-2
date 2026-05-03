<script setup>
import { ref,onMounted, onBeforeUnmount} from 'vue'


const isOpen = ref(false)
const filter_age_range = ref([18, 100])
const filter_radius = ref([1, 100])
const Search = ref('')
const matches = ref([])

function OpenFilter() {
    isOpen.value = true
}

function CloseFilter() {
    isOpen.value = false
}
function handleClickOutside(event) {
    if (Search.value && !Search.value.contains(event.target)) {
        CloseFilter()
    }
}

onMounted(() => {
    document.addEventListener('click', handleClickOutside)
})
onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside)
})

</script>
<template>
    <v-container>
        <section>
            <input type="text" v-model="search" @click='OpenFilter' @focus="OpenFilter"/>
            <div v-if="isOpen" class="filter-dropdown">
                <section class="filter-bar">
                    <div>
                        <label>Age range (Min)</label>
                        <v-range-slider v-model="filter_age_range" :min="18" :max="100" thumb-label="always" />
                    </div>
                    <div>
                        <label>Distance (radius (km))</label>
                        <v-range-slider v-model="filter_radius" :min="1" :max="100" thumb-label="always"  />
                    </div>
               <!--     <div>
                        <label>Interest</label>
                        <div v-for="interest in interests" :key="interest">{{ interest }}</div>
                    </div>-->
                    <div class="filter-footer">
                        <button>Clear Filter(s)</button>
                        <button>Apply Filter(s)</button>
                    </div>
                </section>
            </div>
        </section>
        <div>
            <ul>
                <li v-for="match in matches"><!--It should also say if no filters are applied-->
                    {{ match.name }}
                </li>
            </ul>
        </div>
    </v-container>
</template>