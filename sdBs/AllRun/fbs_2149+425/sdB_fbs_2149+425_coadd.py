from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[327.771583,42.779],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2149+425/sdB_fbs_2149+425_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2149+425/sdB_fbs_2149+425_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
