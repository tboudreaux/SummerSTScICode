from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[292.787083,43.416111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_2M1931+4324/sdB_Kepler_2M1931+4324_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_2M1931+4324/sdB_Kepler_2M1931+4324_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
