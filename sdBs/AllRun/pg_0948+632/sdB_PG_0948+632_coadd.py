from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[148.162292,62.971975],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0948+632/sdB_PG_0948+632_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0948+632/sdB_PG_0948+632_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
