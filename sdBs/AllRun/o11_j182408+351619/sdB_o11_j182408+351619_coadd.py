from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[276.033333,35.271944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j182408+351619/sdB_o11_j182408+351619_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j182408+351619/sdB_o11_j182408+351619_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
