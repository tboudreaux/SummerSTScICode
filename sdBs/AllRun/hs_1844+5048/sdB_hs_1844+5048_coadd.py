from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[281.482417,50.855389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_1844+5048/sdB_hs_1844+5048_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_1844+5048/sdB_hs_1844+5048_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
