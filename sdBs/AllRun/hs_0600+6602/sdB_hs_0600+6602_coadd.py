from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[91.357875,66.038169],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0600+6602/sdB_hs_0600+6602_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0600+6602/sdB_hs_0600+6602_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
