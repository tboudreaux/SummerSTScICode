from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[181.116417,17.462583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_120427.94+172745.3/sdB_SDSSJ_120427.94+172745.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_120427.94+172745.3/sdB_SDSSJ_120427.94+172745.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
