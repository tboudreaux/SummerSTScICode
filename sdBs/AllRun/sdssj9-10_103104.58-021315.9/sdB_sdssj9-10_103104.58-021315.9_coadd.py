from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[157.769083,-2.221083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_103104.58-021315.9/sdB_sdssj9-10_103104.58-021315.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_103104.58-021315.9/sdB_sdssj9-10_103104.58-021315.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
