from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[187.410542,62.594611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_122938.53+623540.6/sdB_sdssj_122938.53+623540.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_122938.53+623540.6/sdB_sdssj_122938.53+623540.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
