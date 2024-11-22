return {
	"goolord/alpha-nvim",
	config = function()
		local alpha = require("alpha")
		local dashboard = require("alpha.themes.dashboard")
		dashboard.section.buttons.val = {
			dashboard.button("e", "   New file", "<cmd>ene <CR>"),
			dashboard.button("SPC f f", "   Find files"),
			dashboard.button("SPC f k", "   Find keymaps"),
			dashboard.button("SPC f w", "   Find current word"),
			dashboard.button("SPC f g", "   Find by grep"),
			dashboard.button("SPC f .", "   List recent files"),
			dashboard.button("SPC f h", "   List help tags"),
		}
		alpha.setup(dashboard.config)
	end,
}
