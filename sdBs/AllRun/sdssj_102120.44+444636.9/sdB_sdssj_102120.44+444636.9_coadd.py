from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[155.335167,44.776917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_102120.44+444636.9/sdB_sdssj_102120.44+444636.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_102120.44+444636.9/sdB_sdssj_102120.44+444636.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
