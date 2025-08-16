
from analysis import get_pca_results, get_sectors, get_1d_pca_results
import matplotlib.pyplot as plt
import streamlit as st
def pca_uis(portfolio):
    st.subheader("PCA Visualization")

    if st.button("Run PCA on Stocks"):
        tickers, pcs, evr, features = get_pca_results(portfolio.stocks, portfolio.simulated_returns)
        sectors = get_sectors(portfolio.stocks, tickers)
        held_tickers = []#get tickers currently held in portfolio (shares > 0)
        for bucket in portfolio.positions.table:
            for ticker, shares in bucket:
                if shares > 0:
                    held_tickers.append(ticker)

        st.write(f"Explained variance ratio: PC1={evr[0]:.2f}, PC2={evr[1]:.2f}")

        fig, ax = plt.subplots(figsize=(10, 7))
        unique_sectors = list(set(sectors))
        colors = plt.cm.get_cmap('tab20', len(unique_sectors))
        for i, sector in enumerate(unique_sectors):#plot all stocks by sector
            xs = [pcs[j, 0] for j in range(len(tickers)) if sectors[j] == sector]
            ys = [pcs[j, 1] for j in range(len(tickers)) if sectors[j] == sector]
            ax.scatter(xs, ys, label=sector, alpha=0.7, color=colors(i))
        held_xs = []#highlight held stocks
        held_ys = []
        for i, ticker in enumerate(tickers):
            if ticker in held_tickers:
                held_xs.append(pcs[i, 0])
                held_ys.append(pcs[i, 1])

        if held_xs and held_ys:
            ax.scatter(
                held_xs,
                held_ys,
                s=150,
                facecolors='none',  #hollow markers
                edgecolors='black',
                linewidths=2,
                label="Held Stocks",
                zorder=5,
            )

        ax.set_xlabel("Principal Component 1")
        ax.set_ylabel("Principal Component 2")
        ax.set_title("PCA of Stocks (Sector, Volatility, Avg Return)")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
    if st.button("Run 1D PCA on Stocks"):#Run 1D PCA and get principal component scores, sectors, and explained variance
            tickers, pc1_scores, sectors, explained_var = get_1d_pca_results(portfolio.stocks, portfolio.simulated_returns)
            held_tickers = [ticker for bucket in portfolio.positions.table for ticker, shares in bucket if shares > 0]
            st.write(f"Explained variance ratio: PC1={explained_var:.2f}")
            fig, ax = plt.subplots(figsize=(10, 3))
            unique_sectors = list(set(sectors)) #assign distinct colors to each sector
            colors = plt.cm.get_cmap('tab20', len(unique_sectors))
            sector_color_map = {sector: colors(i) for i, sector in enumerate(unique_sectors)}
            for sector in unique_sectors: #plot PC1 scores, colored by sector
                xs = [pc1_scores[i] for i in range(len(tickers)) if sectors[i] == sector]
                ys = [0] * len(xs)
                ax.scatter(xs, ys, label=sector, alpha=0.7, color=sector_color_map[sector])
            held_xs = [pc1_scores[i] for i, ticker in enumerate(tickers) if ticker in held_tickers]
            held_ys = [0] * len(held_xs)
            if held_xs:
                ax.scatter(
                    held_xs,
                    held_ys,
                    s=150,
                    facecolors='none',
                    edgecolors='black',
                    linewidths=2,
                    label="Held Stocks",
                    zorder=5,
                )
            ax.set_yticks([])
            ax.set_xlabel("Principal Component 1")
            ax.set_title("1D PCA of Stocks (colored by sector)")
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            ax.grid(True, axis='x')
            st.pyplot(fig)
