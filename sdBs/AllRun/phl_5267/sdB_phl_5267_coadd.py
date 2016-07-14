from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[338.111667,-20.320639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_phl_5267/sdB_phl_5267_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_phl_5267/sdB_phl_5267_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
