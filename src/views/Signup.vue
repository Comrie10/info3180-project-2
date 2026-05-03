<script setup>
    import { ref, onMounted } from "vue";
        
    let csrf_token = ref("");
    
    function getCsrfToken(){
        fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value =data.csrf_token;
            })
    }
    onMounted(() => {
        getCsrfToken();
    })
</script>

<template>
    <v-container>
        <v-form id="SignUpForm" enctype="multipart/form-data" >
        <div class="form-group mb-2">
            <label for="title" class="form-label">Account Sign Up</label>
        </div>
        <div class="form-group mb3">
            <label for="First Name" class="form-label">First Name</label>
            <input type="text" name="first_name" class="form-control"/>
        </div>
        <div class="form-group mb3">
            <label for="Last Name" class="form-label">Last Name</label>
            <input type="text" name="last_name" class="form-control"/>
        </div>
        <div class="form-group mb3">
            <label for="Photo" class="form-label">Photo</label>
            <input type="file" name="photo" class="form-control"/>
        </div>
        <div class="form-group mb3">
            <label for="D_O_B" class="form-label">Date of Birth</label>
            <input type="date" name="date_of_birth" class="form-control"/>
        </div>
        <div class="form-group mb3">
            <label for="Gender" class="form-label">Gender</label>
            <select name="gender" class="form-control" id="gender">
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Trans-Female">Trans-Female</option>
                <option value="Trans-Male">Trans-Male</option>
                <option value="Cis-Female">Cis-Female</option>
                <option value="Cis-Male">Cis-Male</option>
                <option value="Other">Other</option>
            </select>
        </div>
        <div class="form-floating">
            <label for="Email" class="form-label">Email</label>
            <input type="text" name="email" class="form-control"/>
        </div>
        <div class="form-floating">
            <label for="Password" class="form-label">Password</label>
            <input type="text" name="password" class="form-control"/>
        </div>
        <div class="form-floating">
            <label for="Confirm" class="form-label">Confirm Password</label>
            <input type="text" name="confirm" class="form-control"/>
        </div>
        <div>
            <button class="btn btn-lg btn primary w-100 mt-3" type="submit">Sign Up</button>
        </div>
        <div>
        <p>Already have an account?
            <a href="/login">Login here</a>
        </p>
        </div>
    </v-form>
    </v-container>
</template>