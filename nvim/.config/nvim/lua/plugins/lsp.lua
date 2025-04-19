return {
	{
		"williamboman/mason.nvim",
		opts = {},
	},
	{
		"williamboman/mason-lspconfig.nvim",
		dependencies = {
			"williamboman/mason.nvim",
		},
		opts = {
			ensure_installed = {
				"clangd",
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
			lspconfig.clangd.setup({
				capabilities = capabilities,
			})
			lspconfig.lua_ls.setup({
				capabilities = capabilities,
			})
			lspconfig.pylsp.setup({
				capabilities = capabilities,
			})
			vim.keymap.set({ "n", "v" }, "<leader>la", vim.lsp.buf.code_action, { desc = "LSP: Execute code action" })
			vim.keymap.set("n", "<leader>lc", vim.lsp.buf.declaration, { desc = "LSP: Go to declaration" })
			vim.keymap.set("n", "<leader>ld", vim.lsp.buf.definition, { desc = "LSP: Go to definition" })
			vim.keymap.set("n", "<leader>lf", vim.lsp.buf.format, { desc = "LSP: Format code" })
			vim.keymap.set("n", "<leader>lh", vim.lsp.buf.rename, { desc = "LSP: Rename variable" })
			vim.keymap.set("n", "<leader>li", vim.lsp.buf.implementation, { desc = "LSP: Go to implementation" })
			vim.keymap.set("n", "<leader>lk", vim.lsp.buf.hover, { desc = "LSP: Display hover information" })
			vim.keymap.set("n", "<leader>lr", vim.lsp.buf.references, { desc = "LSP: Go to references" })
			vim.keymap.set("n", "<leader>ls", vim.lsp.buf.workspace_symbol, { desc = "LSP: Search workspace symbols" })
			vim.keymap.set("n", "<leader>lt", vim.lsp.buf.type_definition, { desc = "LSP: Go to type definition" })
		end,
	},
}
