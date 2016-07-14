from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[23.441167,13.931556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_013345.88+135553.6/sdB_sdssj_013345.88+135553.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_013345.88+135553.6/sdB_sdssj_013345.88+135553.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
