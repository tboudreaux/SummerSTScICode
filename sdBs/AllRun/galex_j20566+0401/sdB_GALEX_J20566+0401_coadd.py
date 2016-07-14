from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[314.169083,4.023481],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J20566+0401/sdB_GALEX_J20566+0401_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J20566+0401/sdB_GALEX_J20566+0401_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()