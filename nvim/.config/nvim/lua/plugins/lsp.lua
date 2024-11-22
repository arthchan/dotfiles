return {
	{
		"williamboman/mason.nvim",
		opts = {
			ensure_installed = {
				"stylua",
			},
		},
	},
	{
		"williamboman/mason-lspconfig.nvim",
		dependencies = {
			"williamboman/mason.nvim",
		},
		opts = {
			ensure_installed = {
				"lua_ls",
				"pylsp",
			},
		},
	},
	{
		"neovim/nvim-lspconfig",
		config = function()
			local lspconfig = require("lspconfig")
			local capabilities = require("cmp_nvim_lsp").default_capabilities()
			lspconfig.lua_ls.setup({
				capabilities = capabilities,
			})
			lspconfig.pylsp.setup({
				capabilities = capabilities,
			})
			vim.keymap.set("n", "<leader>F", vim.lsp.buf.format, { desc = "LSP: Format code" })
			vim.keymap.set("n", "<leader>D", vim.lsp.buf.type_definition, { desc = "LSP: Go to type definition" })
			vim.keymap.set("n", "<leader>K", vim.lsp.buf.hover, { desc = "LSP: Display hover information" })
			vim.keymap.set("n", "<leader>gd", vim.lsp.buf.definition, { desc = "LSP: Go to definition" })
			vim.keymap.set("n", "<leader>gr", vim.lsp.buf.references, { desc = "LSP: Go to references" })
			vim.keymap.set("n", "<leader>gD", vim.lsp.buf.declaration, { desc = "LSP: Go to declaration" })
			vim.keymap.set("n", "<leader>gI", vim.lsp.buf.implementation, { desc = "LSP: Go to implementation" })
			vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, { desc = "LSP: Rename variable" })
			vim.keymap.set("n", "<leader>ws", vim.lsp.buf.workspace_symbol, { desc = "LSP: Search workspace symbols" })
			vim.keymap.set({ "n", "v" }, "<leader>ca", vim.lsp.buf.code_action, { desc = "LSP: Execute code action" })
		end,
	},
}
