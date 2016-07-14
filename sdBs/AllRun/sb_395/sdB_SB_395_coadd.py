from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[14.798542,-18.300114],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SB_395/sdB_SB_395_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SB_395/sdB_SB_395_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
