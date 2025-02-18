import os
import json
from typing import get_type_hints
from .time import get_current_time
from .args import args
from utils.logging import create_sys_logger
logger = create_sys_logger()

class Configuration():
    # DONT SAVE
    RESULT_TTSG = os.path.join(os.getcwd(),"output/audio/tts_raw.wav")
    RESULT_TTSC = os.path.join(os.getcwd(),"output/audio/tts.wav")
    RESULT_INPUT_SPEECH = os.path.join(os.getcwd(),"output/audio/recorded_speech.wav")
    CONFIG_DIR = os.path.join(os.getcwd(),"configs/components")
    CURRENT_CONFIG_FILENAME = None

    # TTS Conv
    ttsc_url: str = "http://localhost:7865"
    ttsc_voice: str = "my-voice-model"
    ttsc_transpose: int = 0
    ttsc_feature_ratio: float = 0
    ttsc_median_filtering: int = 7
    ttsc_resampling: int = 0
    ttsc_volume_envelope: float = 0
    ttsc_voiceless_protection: float = 0.5

    # Discord
    discord_server_id: str = None


    def update(self, config_d: dict) -> tuple[bool, str]:
        '''
        Returns:
        - If successful: True, None
        - If unsuccessful: False, "failing field"
        '''

        uncommitted = {}
        config_typings = get_type_hints(self)

        # Pre-check fields before committing changes
        try:
            for field in config_d:
                if field not in config_typings:
                    raise Exception(f"Config has no field named: {field}")
                uncommitted[field] = config_typings[field](config_d[field])
        except Exception as err:
            logger.error(f"Could not update config due to error: {err}")
            return False
        
        # Commit config change request
        for field in uncommitted:
            setattr(self, field, uncommitted[field])

        logger.debug("Config update applied without issue.")
        return True

    def save(self, config_d: dict = None, filename: str = None) -> bool:
        config_to_save = config_d
        file_to_save = filename or self.CURRENT_CONFIG_FILENAME
        if config_to_save is None:
            config_to_save = {
                "ttsg_host": self.ttsg_host,
                "ttsg_voice": self.ttsg_voice,
                "ttsc_url": self.ttsc_url,
                "ttsc_voice": self.ttsc_voice,
                "ttsc_transpose": self.ttsc_transpose,
                "ttsc_feature_ratio": self.ttsc_feature_ratio,
                "ttsc_median_filtering": self.ttsc_median_filtering,
                "ttsc_resampling": self.ttsc_resampling,
                "ttsc_volume_envelope": self.ttsc_volume_envelope,
                "ttsc_voiceless_protection": self.ttsc_voiceless_protection,
                "discord_server_id": self.discord_server_id
            }

        try:
            with open(os.path.join(self.CONFIG_DIR, file_to_save), 'w') as f:
                json.dump(config_to_save, f, indent=4)
                logger.info(f"Saved config to {file_to_save}!")
            self.CURRENT_CONFIG_FILENAME = file_to_save
        except Exception as err:
            logger.error(f"Failed to save config to {file_to_save}.json: {err}")
            return False

        return True

    def load(self, filename: str):
        with open(os.path.join(self.CONFIG_DIR, filename), 'r') as f:
            config_d = json.load(f)
        is_ok = self.update(config_d)
        if is_ok:
            self.CURRENT_CONFIG_FILENAME = filename
        return is_ok