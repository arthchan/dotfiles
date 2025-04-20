return {
	"mbbill/undotree",
	config = function()
		if vim.fn.has('win32') then vim.g.undotree_DiffCommand = "FC" end
		vim.keymap.set("n", "<C-u>", vim.cmd.UndotreeToggle, { desc = "Undotree: Toggle Undotree" })
	end,
}
