from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[106.156292,35.380722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0701+355/sdB_fbs_0701+355_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0701+355/sdB_fbs_0701+355_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
