from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[180.102042,-13.014214],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_11578-1244/sdB_EC_11578-1244_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_11578-1244/sdB_EC_11578-1244_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
