const CONSTANTS = {
  API_ENDPOINTS: {
    HEALTH: `${import.meta.env.VITE_API_BASE_URL}/health/`,
  },
  ROUTES: {
    home: "/",
    privacy: "/privacy",
    disclaimer: "/disclaimer",
    charities: "/charities",
    donations: "/donations",
    plan: "/plan",
  },
  SOCIAL: {
    github: "https://github.com/",
    bluesky: "https://bsky.app/",
    discord: "https://discord.gg/Heq7FfUSeN",
    instagram: "https://www.instagram.com/puckcurl",
  },
};

export default CONSTANTS;
