from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[181.03425,15.602694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_120408.22+153609.7/sdB_sdssj_120408.22+153609.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_120408.22+153609.7/sdB_sdssj_120408.22+153609.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
