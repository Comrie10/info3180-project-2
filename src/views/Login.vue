<script>
    
</script>

<template>
    <v-container class="d-flex align-items-center justify-content-center" id="LoginContainer">
        <v-form id="Login" enctype="multipart/form-data">
           <div class="form-group mb-2">
                <label for="title" class="form-label">Login</label>
            </div>
            <div class="form-group mb3"> <!-- look for username/email -->
                <label for="Username" class="form-label">Username</label>
                <input type="text" name="username" class="form-control">
            </div>
            <div class="form-group mb3">
                <label for="password" class="form-label">Password</label>
                <input type="text" name="password" class="form-control">
            </div>
            <div></div>
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
                    <path d="M15.545 6.558a9.4 9.4 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.7 7.7 0 0 1 5.352 2.082l-2.284 2.284A4.35 4.35 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.8 4.8 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.7 3.7 0 0 0 1.599-2.431H8v-3.08z"/>
                </svg>
                <button class="btn btn-lg btn primary w-100 mt-3" type="Submit">Login</button>
            </div>
        </v-form>
    </v-container>
</template>
