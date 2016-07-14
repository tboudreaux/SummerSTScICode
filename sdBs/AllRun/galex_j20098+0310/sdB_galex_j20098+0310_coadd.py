from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[302.464833,3.175489],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j20098+0310/sdB_galex_j20098+0310_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j20098+0310/sdB_galex_j20098+0310_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()