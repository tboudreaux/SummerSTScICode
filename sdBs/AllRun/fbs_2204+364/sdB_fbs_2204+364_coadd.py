from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[331.558792,36.677917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2204+364/sdB_fbs_2204+364_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2204+364/sdB_fbs_2204+364_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
