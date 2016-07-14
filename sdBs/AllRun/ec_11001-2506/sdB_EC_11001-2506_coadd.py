from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[165.6345,-25.373767],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_11001-2506/sdB_EC_11001-2506_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_11001-2506/sdB_EC_11001-2506_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()