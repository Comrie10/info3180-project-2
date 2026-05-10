<script setup>
defineProps({
  message: Object,
  currentUserId: Number
})
</script>

<template>
  <div
    class="message-wrapper"
    :class="{
      outgoing: message.sender_id === currentUserId,
      incoming: message.sender_id !== currentUserId
    }"
  >
    <div class="message-bubble">
      <p>{{ message.content }}</p>

      <span class="time">
        {{ message.time }}
      </span>
    </div>
  </div>
</template>

<style scoped>
.message-wrapper {
  display: flex;
  margin-bottom: 18px;
}

.incoming {
  justify-content: flex-start;
}

.outgoing {
  justify-content: flex-end;
}

.message-bubble {
  max-width: 380px;
  padding: 14px 18px;
  border-radius: 20px;
  position: relative;
}

.incoming .message-bubble {
  background: #f3f3f3;
  color: #333;
}

.outgoing .message-bubble {
  background: #ff2d75;
  color: white;
}

.message-bubble p {
  line-height: 1.5;
  margin-bottom: 8px;
}

.time {
  font-size: 11px;
  opacity: 0.7;
}
</style>