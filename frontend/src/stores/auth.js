import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    profile: null
  }),

  actions: {

    async login(email, password) {
      const res = await axios.post(
        'http://localhost:5000/auth/login',
        { email, password },
        { withCredentials: true }
      )

      this.user = res.data.user

      await this.fetchUser()

      return res.data
    },

    async fetchUser() {
      const res = await axios.get(
        'http://localhost:5000/auth/me',
        { withCredentials: true }
      )

      this.user = res.data.user

      // optional: if backend returns profile
      this.profile = res.data.profile || null
    },

    logout() {
      this.user = null
      this.profile = null
    }
  }
})