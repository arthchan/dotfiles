return {
	"mbbill/undotree",
	config = function()
		vim.keymap.set("n", "<C-u>", vim.cmd.UndotreeToggle, { desc = "Undotree: Toggle Undotree" })
	end,
}
