<template>
    <div>
        <form>Login Page
            <div class="form-group">
                <label for="Username"></label>
                <input type="text" class="form-control">
            </div>
            <div class="form-group">
                <label for="Password"></label>
                <input type="password" class="form-control">
            </div>
            <div class="my-3"></div>
            <button type="submit" class="btn btn-primary">
                Login
            </button>
        </form>
    </div>
</template>
<script>
export default {
    name: 'UserLogin'
};
</script>